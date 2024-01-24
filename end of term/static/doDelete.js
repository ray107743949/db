
export default function doDelete(id) {
    let data = { "id": id };
    axios.post('dodelete', Qs.stringify(data))
        .then(res => {
            document.getElementById("content").innerHTML = res['data']
            
        })
        .catch(err => {
            document.getElementById("content").innerHTML = err;
        })
    }