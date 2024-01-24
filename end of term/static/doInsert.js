
export default function doInsert() {
    let data = {
        "name": document.getElementById("name").value,
        "gender": document.getElementById("gender").value,
        "age": document.getElementById("age").value,
        "nation": document.getElementById("nation").value,
        "county": document.getElementById("county").value,
        "township": document.getElementById("township").value,
        'position_id': document.getElementById("position").value
    }
    console.log(data)
    axios.post("doinsert", Qs.stringify(data))
        .then(res => {
            let result = res['data'];
            const content = document.getElementById("content");
            content.innerHTML = result;
        })
        .catch(err => {
            document.getElementById("content").innerHTML = err;
        })
}