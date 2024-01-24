export default function starPage() {
    const str = `<div id="head">
<button id="president">總統</button>
<button id="county_magistrate">地方首長</button>
<button id="township">區(鄉)長</button>
<button id="legislator">立法委員</button>
</div>
<div id="content">`
    document.getElementById('root').innerHTML = str
}