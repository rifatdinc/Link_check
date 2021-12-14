import React, { useState } from 'react'
import { Input ,message, Button, Table, Form, Row } from 'antd'
import axios from 'axios'

const Signalscan = () => {
    const [data, setdata] = useState([])
    const [Scanreal, setScanreal] = useState([])
    const [selectionType] = useState('radio');
    const [Realspeed, setRealspeed] = useState([])
    const [Dataclicks, setDataclicks] = useState([])

    const rowSelection = {
        onChange: (selectedRowKeys, selectedRows) => {
            setDataclicks(selectedRows)
            console.log(`selectedRowKeys: ${selectedRowKeys}`, 'selectedRows: ', selectedRows);
        }
    }


    function formatBytes(bytes) {
        var marker = 1024; // Change to 1000 if required
        var decimal = 3; // Change as required
        var kiloBytes = marker; // One Kilobyte is 1024 bytes
        var megaBytes = marker * marker; // One MB is 1024 KB
        var gigaBytes = marker * marker * marker; // One GB is 1024 MB
        // var teraBytes = marker * marker * marker * marker; // One TB is 1024 GB

        // return bytes if less than a KB
        if (bytes < kiloBytes) return bytes + " Bytes";
        // return KB if less than a MB
        else if (bytes < megaBytes) return (bytes / kiloBytes).toFixed(decimal) + " KB";
        // return MB if less than a GB
        else if (bytes < gigaBytes) return (bytes / megaBytes).toFixed(decimal) + " MB";
        // return GB if less than a TB
        else return (bytes / gigaBytes).toFixed(decimal) + " GB";
    }


    const columns = [
        {
            title: 'Accespoint',
            dataIndex: 'Accespoint',
            render: (text) => <i>{text}</i>,
        },
        {
            title: 'Signal',
            dataIndex: 'Signal',
        },
        {
            title: 'Frequency',
            dataIndex: 'Frequency',
        },
    ];
    const Realdata = () => {
        const idip = document.getElementById('register_email').value
        const payload = {
            "Ipadress": idip
        }
        axios.post('http://localhost:5000/realdatascan', payload)
            .then(res => setScanreal(res.data))



    }
    const queryselectors = () => {
        const Accespint = Dataclicks[0].Accespoint
        const ppoename = document.getElementById('ppoename1').innerText
        const Frequency = Dataclicks[0].Frequency
        const idip = document.getElementById('register_email').value

        const payload = {
            "pppoename": ppoename,
            "Accespoint": Accespint,
            "Ipadress": idip,
            "Frequency": Frequency,
        }
        axios.post('http://localhost:5000/scanconnect', payload)
            .then(res => setRealspeed(res.data))

    }

    const qreuests = () => {
        Realdata()
        setTimeout(() => {
            const ip = document.getElementById('register_email').value
            if (ip === '') {
                message.error('Ip bos olamaz.');
            }
            const payload = { "Data": ip }
            axios.post('http://localhost:5000/signalscan', payload)
                .then((res) => {
                    console.log(res.data)
                    setdata(res.data)
                })
        }, 1000);


    }
    return (
        <div className="container">
            {/* {console.log(data)}
            {data.Costumerinfo !== [] ?  <Row>
                <p>Bagli Oldugu Acces Point{data.Costumerinfo[0]['radioname']}</p>
                <p>{data.Costumerinfo[0]['sig2']} / {data.Costumerinfo[0]['sig1']}</p>
                <p>{data.Costumerinfo[0]['sig3']} / {data.Costumerinfo[0]['sig4']} </p>
            </Row>: null } */}

            <div>
                <h1 className="text-center">Sinyal Tarama</h1>
                <Form name="register">
                    <Form.Item name="email" label="Ip Adress Giriniz">
                        <Input />
                    </Form.Item>
                </Form>
                <Button className="d-inline-flex" onClick={qreuests}> Sinyal Tara </Button>
            </div>

            {Scanreal.length > 0 ?
                <div className="bordered">


                    <Row>
                        <table className="table table-sm">
                            <thead>
                                <tr>
                                    <th scope="col">Kullanici Adi</th>
                                    <th scope="col">Sinyaller</th>
                                    <th scope="col">Bagli Oldugu Ap</th>
                                </tr>
                            </thead>
                            <tbody>

                                <tr>
                                    <td id="ppoename1" >{Scanreal[0]['ppoename']}</td>
                                    <td>{Scanreal[0]['sig1']} /  {Scanreal[0]['sig2']} / {Scanreal[0]['sig3']} /  {Scanreal[0]['sig4']}</td>
                                    <td>{Scanreal[0]['radioname']} </td>
                                </tr>
                                {Realspeed.map((e) => {
                                    return <tr>
                                        <td>{ e.status } </td>
                                        <td>{e.duration}</td>
                                        <td>{formatBytes(e['rx-current'])}</td>
                                    </tr> 
                                })}


                            </tbody>
                        </table>
                        {/* {console.log(Scanreal)}
                        <Col span={12}></Col>
                        <Col span={12}></Col>
                        <Col span={12}></Col>
                        <Col span={12}></Col>
                        <Col span={12}></Col>
                        <Col span={12}> </Col> */}

                        <div>
                        </div>
                    </Row>
                </div>
                : null
            }
            {console.log(Realspeed)}
            {Realspeed.length > 0 ? console.log(Realspeed.Donus) : null}





            <Table
                rowSelection={{
                    type: selectionType,
                    ...rowSelection,
                }}
                bordered={true}
                columns={columns}
                dataSource={data}
            />
            { data ?
                <div>

                    <button onClick={queryselectors} className="btn btn-success border">
                        Baglan
            </button>

                </div>
                : null}



        </div>

    )
}

export default Signalscan


// // {console.log(data)}
// self.responses = {}
// for url in self.urlsapi(ip):
//     url = url.format(ip)
//     # print(url)

//     r = s.get(
//         url=url,
//         verify=False
//     )

//     self.responses.update(
//         {"Ip": ip, "Data1": r.json() if r.status_code == 200 else r.status_code})
// self.responses_by_ip.update({"Data": self.responses})
// return self.responses_by_ip