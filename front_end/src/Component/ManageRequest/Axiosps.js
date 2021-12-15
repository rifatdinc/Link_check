import axios from "axios";

const Nasdataccr = async () => {
    try {
        const res = await axios.get('http://192.168.192.102:5000/nasdata');
        return await res.data;
    } catch (err) {
        return console.log(err);
    }
}

const Mimosa = async (payload) => {
    try {
        const res = await axios.post('http://192.168.192.102:5000/getdatasql', payload);
        if (res.data) {
            return res.data
        } else {
            return res.data = []
        }
    } catch (err) {
        return console.log(err);
    }
}

const Ubnt5gHz = async (payload) => {
    try {
        const res = await axios.post('http://192.168.192.102:5000/ubnt5gHz', payload);
        if (res.data !== null) {
            return res.data;
        }

    } catch (err) {
        return console.log(err);
    }
}

const Ubnt60ghz = async () => {
    const res = await axios.get('http://192.168.192.102:5000/ubnt60ghz');
    return res.data;
}

const SpeakSignal = async (payload) => {
    try {

        const res = await axios.post('http://192.168.192.102:5000/Speaksignal', payload)
        if (res.data !== null) {

            return res.data
        }
    } catch (error) {
        console.log(error);
    }
}

const Mikrotikreq = async (payload) => {
    try {
        const res = await axios.post('http://192.168.192.102:5000/mikrotik', payload)
        return res.data
    } catch (error) {
        console.log(error);
    }
}

const Mikrotik60ghz = async () => {
    try {
        const res = await axios.get('http://192.168.192.102:5000/Mik60ghz')

        return res.data['Data']
    } catch (error) {
        console.log(error);
    }
}

const ExportedFunc = {
    Nasdataccr,
    Mimosa,
    Ubnt5gHz,
    Ubnt60ghz,
    SpeakSignal,
    Mikrotikreq,
    Mikrotik60ghz
}
export default ExportedFunc