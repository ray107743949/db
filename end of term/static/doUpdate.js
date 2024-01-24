
export default function doUpdate(id) {
    let data = {
        "id": id,
        "name": document.getElementById("name").value,
        "gender": document.getElementById("gender").value,
        "age": document.getElementById("age").value,
        "nation": document.getElementById("nation").value,
        "county": document.getElementById("county").value,
        'position_id': document.getElementById("position_id").value,
        "township": document.getElementById("townships").value,
    };
    console.log(data)
    axios.post('doupdate', Qs.stringify(data))
        .then(res => {
            let response = res['data'];

            document.getElementById("content").innerHTML = response;

        })
        .catch(err => {
            document.getElementById("content").innerHTML = err;

        })
}

