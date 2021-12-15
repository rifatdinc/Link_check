import React, { useEffect, useState } from 'react'
import { List, Card, Row, Col } from 'antd';
import WifiIndicator, { DBMToSignalStrength } from 'react-wifi-indicator';
import ClimbingBoxLoader from "react-spinners/ClimbingBoxLoader";
import { css } from "@emotion/react";
import Axiosps from '../ManageRequest/Axiosps'
const Mik60Ghz = () => {
    const [Mikd60, setMikd60] = useState([])

    const override = css`
    display: block;
    margin: 0 auto;
    border-color: red;
    align-items: center; `;

    useEffect(() => {

        const interva = setInterval(() => {
            Axiosps.Mikrotik60ghz().then((res)=>{
                setMikd60(res)}).catch(err => console.log(err))
        }, 5000)
        return () => clearInterval(interva)

    }, [])

    return (
        <div>

            {Mikd60 && Mikd60.length > 0 ? <div>
                <List

                    grid={{ gutter: 16, xs: 1, sm: 2, md: 4, lg: 4, xl: 6, xxl: 4, }}
                    rowKey={Math.random()}

                    dataSource={Mikd60}
                    renderItem={item => (

                        <List.Item id="Cardbolumu" bordered="true" style={{ width: "450px" }} >
                            <Card size="small">

                                <Row>
                                    <Col span={8}>
                                        <a className="text-right" href={`http://${item.Ipadres}`} > {item.Ipadres} </a>

                                        <div>{item.system[0]['DeviceName']}</div>
                                        <div>Cpu {item.system[0]['Cpu']} %</div>
                                        <div style={{ fontSize: "11px" }} >Uptime {item.system[0]['Uptime']}</div>
                                    </Col>
                                    <Col span={8} offset={8}>
                                        <div> Wireless Disable  {item.wireless[0]['Wireless_Disable'] !== 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                        <div> Ethernet Disable  {item.Ethernet[0]['Ethernet_Disable'] !== 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                        <div> Wireless Running  {item.wireless[0]['Wireless_Running'] === 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                        <div> Ethernet Running  {item.Ethernet[0]['Ethernet_Running'] === 'false' ? <i class="fas fa-times"></i> : <i class="fas fa-check"></i>}</div>
                                    </Col>
                                </Row>

                                <hr />
                                <table className="table table-sm">
                                    <thead>
                                        <tr>
                                            <th scope="col"></th>
                                            <th scope="col">Model</th>
                                            <th scope="col"></th>
                                            <th scope="col" className="text-right">{item.system[0]['BoardName']}</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Ethernet Hizi </td>
                                            <td></td>
                                            <td className="text-right">{item.Ethernet[0]['EthernetRate']}</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Frequency </td>
                                            <td></td>
                                            <td className="text-right"> {item.Wlandata[0]['frequency']} gHz </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Anlik Upload / Anlik Download </td>
                                            <td></td>
                                            <td className="text-right"> {item.Getcurrent["Rx"]} / {item.Getcurrent["Tx"]} </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Ethernet / Wireless Kopma </td>
                                            <td></td>
                                            <td className="text-right"> {item.Interface[0]['link-downs']} / {item.Interface[1]['link-downs']} </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Uzaklık </td>
                                            <td></td>
                                            <td className="text-right"> {item.Wlandata[0]['distance']} m </td>
                                        </tr>

                                        <tr>
                                            <th scope="row"></th>
                                            <td>Yazilim </td>
                                            <td></td>
                                            <td className="text-right"> {item.system[0]['Firmware']} </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Wlan Mod / Frekans Mod</td>
                                            <td></td>
                                            <td className="text-right"> {item.wireless[0]['Wireless_Mode']} / {item.wireless[0]['Wireless_Frequency']}  </td>
                                        </tr>

                                        <tr>
                                            <th scope="row"></th>
                                            <td> Sinyal Kuvveti Rx</td>
                                            <td></td>

                                            <td className="text-right">{item.Wlandata[0]['rssi']}  <WifiIndicator strength={DBMToSignalStrength(item.Wlandata[0]['rssi'])} /></td>
                                        </tr>

                                    </tbody>
                                </table>
                            </Card>
                        </List.Item>)} />
            </div> : <ClimbingBoxLoader css={override} size={30} color={"#123abc"} />}
        </div>
    )
}

export default Mik60Ghz
