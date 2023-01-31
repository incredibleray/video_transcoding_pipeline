const elems=$("table").getElementsByTagName("a"); let urls=[]; for (let i=0; i<elems.length; i++) {if (elems[i].hasAttribute("href")) {urls.push(elems[i].href)}}; JSON.stringify(urls)

// mp3
const elems=$("table")[2].getElementsByTagName("a"); let urls=[]; for (let i=0; i<elems.length; i++) {if (elems[i].hasAttribute("href")) {urls.push(elems[i].href)}}; JSON.stringify(urls)