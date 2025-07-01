document.getElementById("summarize").addEventListener("click", async () => {
  const status = document.getElementById("status");
  const video = document.getElementById("brainrotVideo");
  const videoSource = video.querySelector("source");
  const subtitlesDiv = document.getElementById("subtitles");
  const videoContainer = document.getElementById("video-container");

  status.innerHTML = `<p>Generating summary... <span class="spinner"></span></p>`;
  subtitlesDiv.innerText = "";
  videoContainer.style.display = "none";

  chrome.tabs.query({ active: true, currentWindow: true }, (tabs) => {
    chrome.scripting.executeScript({
      target: { tabId: tabs[0].id },
      func: () => document.body.innerText
    }, async (results) => {
      const MAX_LENGTH = 4000;
      const pageText = results[0].result.slice(0, MAX_LENGTH);

      try {
        const res = await fetch("http://localhost:5000/api/summarize", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ text: pageText })
        });

        const data = await res.json();

        if (data.summary) {
          status.innerHTML = `<p><strong>Summary:</strong></p>`;
          const summaryText = document.createElement("pre");
          summaryText.innerText = data.summary;
          summaryText.style.whiteSpace = "pre-wrap";
          summaryText.style.wordBreak = "break-word";
          status.appendChild(summaryText);

          videoSource.src = `http://localhost:5000${data.video}`;
          video.load();

          const audio = new Audio(`http://localhost:5000${data.audio}`);
          const subtitleRes = await fetch(`http://localhost:5000${data.subtitles}`);
          const subtitles = await subtitleRes.json();

          // Subtitles rendering
          const renderSubtitles = () => {
            const time = audio.currentTime;
            const active = subtitles.find(s => time >= s.start && time <= s.end);
            subtitlesDiv.innerText = active ? active.text : "";
            requestAnimationFrame(renderSubtitles);
          };

          requestAnimationFrame(renderSubtitles);

          audio.play();
          video.play();
          videoContainer.style.display = "block";
        } else {
          status.innerText = "Failed to generate summary.";
        }
      } catch (err) {
        console.error(err);
        status.innerText = "Error contacting server.";
      }
    });
  });
});
