function get_lunch() {
    fetch('/lunch').then((res) => res.json()).then((data) => {
        console.log(data)
    })
}

get_lunch()