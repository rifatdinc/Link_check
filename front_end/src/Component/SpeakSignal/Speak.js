import React, { useEffect, useState } from 'react'
import Axiosps from '../ManageRequest/Axiosps'
import { Input, Form, Button, Spin } from 'antd';
const Zorlakonusutur = () => {
    const [Dataa, setDataa] = useState([])
    const [TargerSignal, setTargerSignal] = useState('')
    const [Check, setCheck] = useState(true)

    const Dataqets = () => {
        setTargerSignal(document.getElementById('IpaddressSpeak').value)
        setCheck(true)
    }
    const Stopted = () => {
        setCheck(false)
        console.log('xx')
    }
    useEffect(() => {
        if (Check) {
            if (TargerSignal.length > 0) {
                const Paylod = { "IpaddressSpeak": TargerSignal }
                var Intervals1 = setInterval(() => {
                    Axiosps.SpeakSignal(Paylod).then(res => {
                        if (res) {
                            console.log(res)
                            var msg = new SpeechSynthesisUtterance(res[0])
                            msg.lang = 'tr-TR'
                            window.speechSynthesis.speak(msg)
                            setDataa(res)

                        }
                    }).catch(err => console.log(err))
                }, 2000);
            } else {
                clearInterval(Intervals1)
            }
            return () => {
                clearInterval(Intervals1)
                setDataa([])
            }
        }

    }, [Check, TargerSignal])

    return (
        <div >
            <h3 className='text-center mt-3' >Signal Speaker</h3>
            <Form className='mt-5'>
                <Form.Item>
                    <Input id="IpaddressSpeak" placeholder="Ip adresi giriniz Ornegin : 10.23.1.245" />
                </Form.Item>
            </Form>
            {Dataa.length > 0 && Dataa.map((e) => <h1 className='text-center'>{e}</h1>)}
            <Button type='primary' className='mb-2' block onClick={Dataqets}> Baslat</Button>
            <Button type='danger' block onClick={Stopted}> Durdur</Button>
        </div>
    )
}

export default Zorlakonusutur
