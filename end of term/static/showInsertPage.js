import doInsert from './doInsert.js'
export default function showInsertPage(){
    document.getElementById('content').innerHTML = `
        <div class="insert">
        <center>
        姓名：<input type="text" id="name"><br>
        性別：<input type="text" id="gender"><br>
        年齡：<input type="text" id="age"><br>
        職位：<input type="text" id="position"><br>
        國籍：<input type="text" id="nation"><br>
        縣市：<input type="text" id="county"><br>
        鄉鎮：<input type="text" id="township"><br>

        </center>
        <br>
        <center><button id="doinsert1">新增</button></center>
        </div>`
        document.getElementById('doinsert1').onclick = function(){
           doInsert();
        }
    }
