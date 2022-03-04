import axios from "axios";
import return401 from "../../utils/return401";

const funcToken = () => {
    const token1 = localStorage.getItem('tokens')
    const tokens = { headers: { "Authorization": `Bearer ${token1}` } }
    
    return tokens
}

const Nasdataccr = async () => {
    try {
        const res = await axios.get('http://192.10.10.180:5000/nasdata', funcToken());
        return res.data;
    } catch (error) {
        return401(error)

    }
}

const Nasdatavalue = async () => {
    try {
        const res = await axios.get('http://192.10.10.180:5000/nasdatavalue', funcToken());
        return res.data;
    } catch (error) {
        return401(error)
    }
}


const Mimosa = async (payload) => {
    try {
        const res = await axios.post('http://192.10.10.180:5000/getdatasql', payload, funcToken());
        if (res.data) {
            return res.data
        } else {
            return res.data = []
        }
    } catch (error) {
        return401(error)

    }
}

const Ubnt5gHz = async (payload) => {
    try {
        const res = await axios.post('http://192.10.10.180:5000/ubnt5gHz', payload, funcToken());
        if (res.data !== null) {
            return res.data;
        }

    } catch (error) {
        return401(error)

    }
}

const Ubnt60ghz = async () => {

    try {
        const res = await axios.get('http://192.10.10.180:5000/ubnt60ghz', funcToken());
        return res.data;
    } catch (error) {
        return401(error)

    }
}

const SpeakSignal = async (payload) => {

    try {

        const res = await axios.post('http://192.10.10.180:5000/Speaksignal', payload, funcToken())
        if (res.data !== null) {

            return res.data
        }
    } catch (error) {
        return401(error)
    }
}

const Mikrotikreq = async (payload) => {

    try {
        const res = await axios.post('http://192.10.10.180:5000/mikrotik', payload, funcToken())
        return res.data
    } catch (error) {
        return401(error)
    }
}

const Mikrotik60ghz = async () => {

    try {
        const res = await axios.get('http://192.10.10.180:5000/Mik60ghz', funcToken())
        return res.data
    } catch (error) {
        return401(error)
    }
}

const Find_Fail = async (payload) => {

    try {
        const res = await axios.post('http://192.10.10.180:5000/find_fail', payload, funcToken())
        return res.data
    } catch (error) {
        return401(error)
    }

}

const Login = async (payload) => {
    try {
        const res = await axios.post('http://192.10.10.180:5000/Login', payload)
        return res.data
    } catch (error) {
        return401(error)
    }
}

const ExportedFunc = {
    Nasdataccr,
    Mimosa,
    Ubnt5gHz,
    Ubnt60ghz,
    SpeakSignal,
    Mikrotikreq,
    Mikrotik60ghz,
    Find_Fail,
    Login,
    Nasdatavalue
}
export default ExportedFunc