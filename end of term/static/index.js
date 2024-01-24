import select_position from "./select_position.js"
import starPage from "./starpage.js"


window.onload = function () {
    starPage()


    document.getElementById('president').onclick = function () {
        select_position(1, '總統')
    }

    document.getElementById('county_magistrate').onclick = function () {
        select_position(2, '地方首長')
    }

    document.getElementById('township').onclick = function () {
        select_position(3, '區(鄉)長')
    }

    document.getElementById('legislator').onclick = function () {
        select_position(4, '立法委員')
    }

}


