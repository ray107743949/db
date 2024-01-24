import doUpdate from './doUpdate.js';

export default function showUpdatePage(id) {

    let data = {
        "id": id
    };
    axios.post('select_id', Qs.stringify(data))
        .then(res => {
            const row = res['data'][0];
            let str = `<center>
            姓名：<input type="text" id="name" value="` + row[0] + `" ><br>`;
            str += `姓名：<input type="text" id="gender" value="` + row[1] + `"><br>`;
            str += `職別：<input type="text" id="position_id" value="` + row[2] + `"><br>`;
            str += `年齡：<input type="text" id="age" value="` + row[3] + `"><br>`;
            str += `國籍：<input type="text" id="nation" value="` + row[4] + `"><br>`;
            str += `縣市：<input type="text" id="county" value="` + row[5] + `"><br>`;
            str += `地區：<input type="text" id="townships" value="` + row[6] + `"><br>`;
            str += `</center>`;
            str += `<center><button id="doUpdate2">確定修改</button></center>`;
            document.getElementById("content").innerHTML = str;
            document.getElementById("doUpdate2").onclick = function () {
                doUpdate(id)
            }
        })

        .catch(err => {
            console.log(err)
        })
}