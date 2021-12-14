/* eslint-disable array-callback-return */
import React, { useEffect, useState } from 'react'
import Speech from 'react-speech';
import Axiosps from '../Axioss/Axiosprocess'
import { Input, Form, Button } from 'antd';

const Zorlakonusutur = () => {
    const [Dataa, setDataa] = useState([])
    const [TargerSignal, setTargerSignal] = useState('')

    const Dataqets = () => {
        setTargerSignal(document.getElementById('IpaddressSpeak').value)
    }

    const Dataokut = () => {
        try {
            if (TargerSignal.length > 0) {
                setTimeout(() => {
                    document.getElementsByClassName("rs-play")[0].click()
                    
                }, 2000);
            }
        } catch (error) {
            console.log(error);
        }
    }

    useEffect(() => {
        if (TargerSignal.length > 0) {
            const Paylod = { "IpaddressSpeak": TargerSignal }
            var Intervals1 = setInterval(() => {
                Axiosps.SpeakSignal(Paylod).then(res => {
                    if (res) {
                        setDataa(res)
                    }


                }).catch(err => console.log(err))
            }, 2000);

            return () => {
                clearInterval(Intervals1)
                setDataa([])

            }
        }

    }, [TargerSignal])

    return (
        <div>
            <Form>
                <Form.Item>
                    <Input id="IpaddressSpeak" placeholder="Ip adresi giriniz Ornegin : 10.23.1.245" />
                </Form.Item>
            </Form>
            <Button onClick={Dataqets}> Baslat</Button>
            <Button> Durdur</Button>

            {Dataa.map((e) => {
                return <div id="Starts1">
                    <Speech
                        key={Math.random()}
                        text={e}
                        rate="1"
                        textAsButton={true}
                        displayText="Baslat"
                        lang="tr-TR"
                        voice="Google TR Turkish Female" />
                </div>
            })}
            {Dataa.length > 0 ? Dataokut():console.log("Data Okut")}
           
        </div>
    )
}

export default Zorlakonusutur
