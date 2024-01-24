import doDelete from './doDelete.js';
export default function president() {
    let data = {
        'id' : 1
    }
    console.log(data)
    axios.post('select', Qs.stringify(data))
        .then(res => {
            const result =res['data']
            let str = `<h1>總統</h1><table>`;
            str +=
            `<tr style="background-color: #ffffff;">
            <td>名子</td><td>性別</td><td>年齡</td><td>國籍</td><td>縣市</td><td>地區</td><td colspan="2" ><center><button id='doinsert'>新增</button></center></td>
            </tr>`
            for (let i = 0; i < result.length; i++) {
                str += `<tr>`;
                str += `<td name='id'>` + result[i][0] + `</td>`;
                for (let j = 1; j < result[i].length; j++) {

                    str += `<td>` + result[i][j] + `</td>`;
                }
                str += `<td><button name='doupdate'>修改</button></td>`;
                str += `<td><button name='dodelete'>刪除</button></td>`;
                str += `</tr>`;
            };
            str += `</table>`;
            document.getElementById('content').innerHTML = str;
            document.getElementById('content').innerHTML = str;
            document.getElementById("doinsert").onclick = function () {
                showInsertPage();
            };
            const ids = document.getElementsByName('id');

            const doupdate = document.getElementsByName("doupdate");
            for (let i = 0; i < doupdate.length; i++) {
                doupdate[i].onclick = function () {
                    showUpdatePage(ids[i].innerText);
                };
            }

            const dodelete = document.getElementsByName("dodelete");
            for (let i = 0; i < dodelete.length; i++) {
                dodelete[i].onclick = function () {
                    // console.log(ids[i].innerText)
                    doDelete(ids[i].innerText);
                };
            }
        })
        .catch(err => {
            console.error(err);
        })
}