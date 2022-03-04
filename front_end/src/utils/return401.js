
const return401 = (error) => {
    if (error.response.status === 401) {
        localStorage.removeItem('tokens')
        window.location.replace("/Login")
    }
}

export default return401