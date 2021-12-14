import React, { useEffect, useState } from 'react'
import { List, Card, Row, Col } from 'antd';
import WifiIndicator, { DBMToSignalStrength } from 'react-wifi-indicator';
import formatBytes from './Formatbytes';
import secondsToDhms from './secondToDhms';
import Axiosprocess from './Axioss/Axiosprocess'

const Ubnt60ghz = () => {
    const [Dataubnt, setDataubnt] = useState([])

    useEffect(() => {
        const interva = setInterval(() => {
            Axiosprocess.Ubnt60ghz().then(res => { setDataubnt(res) })
        }, 5000)
        return () => {

            setDataubnt([])
            clearInterval(interva)
        }

    }, [])

    return (
        <div>
            <List
                grid={{ gutter: 16, column: 4 }}
                dataSource={Dataubnt}
                renderItem={((item) => {
                    try {
                        return <List.Item>
                            <Card >
                                <Row>
                                    <Col span={8}>
                                        <a className="text-right" href={`http://${item.Data["Ip"]}`} > {item.Data["Ip"]} </a>
                                        <div>{(item.Data.Data1["host"]["hostname"])}</div>
                                        <div> </div>
                                    </Col>
                                    <Col span={8} offset={8}>
                                        <div> Ethernet Disable  {item.Data.Data1.interfaces[0].status['plugged'] === 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                        <div> Wireless Disable  {item.Data.Data1.interfaces[3].status['enabled'] === 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                    </Col>
                                </Row>
                                <div style={{ fontSize: "12px" }} >Uptime {secondsToDhms(item.Data.Data1["host"]["uptime"])}</div>
                                <hr />
                                <table className="table table-sm">
                                    <thead>
                                        <tr>
                                            <th scope="col"></th>
                                            <th scope="col">Capacity</th>
                                            <th scope="col"></th>
                                            <th scope="col" className="text-right"> {formatBytes(item.Data.Data1.wireless.sta[0]["prs_sta"]['capacity'] + "000")}</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Device Model </td>
                                            <td></td>
                                            <td className="text-right">{item.Data.Data1["host"]["devmodel"]}</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Ethernet Speed </td>
                                            <td></td>
                                            <td className="text-right">{item.Data.Data1.interfaces[0].status["speed"]}</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Frequency </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.wireless.prs_info["frequency"]} gHz </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Upload / Download </td>
                                            <td></td>
                                            <td className="text-right"> {formatBytes(item.Data.Data1.wireless.throughput["rx"] + "000")} / {formatBytes(item.Data.Data1.wireless.throughput["tx"] + "000")} </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Anten Gain </td>
                                            <td></td>
                                            <td className="text-right"> {(() => {
                                                if (item.Data.Data1["host"]["devmodel"] === "airFiber 60 LR") {
                                                    return (
                                                        <>{item.Data.Data1.wireless.sta[0].remote.prs_remote["antenna_gain"]}</>
                                                    )
                                                } else if (item.Data.Data1["host"]["devmodel"] === "GigaBeam LR") {
                                                    return (<>{item.Data.Data1.wireless["antenna_gain"]}</>)
                                                } else if (item.Data.Data1["host"]["devmodel"] === "airFiber 60") {
                                                    return (
                                                        <>{item.Data.Data1.wireless["antenna_gain"]}</>
                                                    )
                                                }
                                            })()} dBi</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Mac Adress </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.interfaces[1]['hwaddr']} </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Distance </td>
                                            <td></td>
                                            <td className="text-right">{(() => {
                                                if (item.Data.Data1["host"]["devmodel"] === "airFiber 60 LR") {
                                                    return (
                                                        <>{item.Data.Data1.wireless.sta[0].prs_sta["distance"]}</>
                                                    )
                                                } else if (item.Data.Data1["host"]["devmodel"] === "GigaBeam LR") {
                                                    return (
                                                        <>{item.Data.Data1.wireless["distance"]}</>
                                                    )
                                                } else if (item.Data.Data1["host"]["devmodel"] === "airFiber 60") {
                                                    return (
                                                        <>{item.Data.Data1.wireless.sta[0].prs_sta["distance"]}</>
                                                    )
                                                }
                                            })()}  Metre </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Wlan Mode </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1["host"]["netrole"]}</td>
                                        </tr>

                                        <tr>
                                            <th scope="row"></th>
                                            <td> Signal Strength Rx</td>
                                            <td></td>

                                            <td className="text-right">{item.Data.Data1.wireless.sta[0]["prs_sta"]['rssi_data']}  <WifiIndicator strength={DBMToSignalStrength(item.Data.Data1.wireless.sta[0]["prs_sta"]['rssi_data'])} /></td>
                                        </tr>

                                    </tbody>
                                </table>
                            </Card>
                        </List.Item>
                    } catch (error) {
                        console.log(error)
                    }
                })}
            />
        </div>
    )
}

export default Ubnt60ghz
