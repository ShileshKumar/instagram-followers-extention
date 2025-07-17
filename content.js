// content.js
chrome.runtime.onMessage.addListener((req, sender, sendResponse) => {
  if(req.type === "getFollowers") {
    // Read DOM or XHR for followers (see extension dev docs for details)
    sendResponse({followers: [], following: []}); // Replace with real data!
  }
});
