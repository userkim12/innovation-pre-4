function get_advice() {
    fetch('/advice').then((res) => res.json()).then((data) => {
        console.log(data)
    })
}

get_advice()