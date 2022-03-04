import React, { useEffect, useState } from 'react'
import { List, Card, Row, Col, Menu, Layout, Breadcrumb } from 'antd';
import WifiIndicator, { DBMToSignalStrength } from 'react-wifi-indicator';
import Axiosproces from '../ManageRequest/Axiosps';
import { Tabs } from 'antd';

const { TabPane } = Tabs;
const { Content, Sider } = Layout;

const Mikrotik = () => {
    const [Mikda, setMikda] = useState([])
    const [Sqldata, setSqldata] = useState([])
    const [Loading, setLoading] = useState(false)
    const [activeItem, setactiveItem] = useState({ activeItem: "Balturk 1" })

    const [Target, setTarget] = useState('')
    useEffect(() => {
        setLoading(true)
        Axiosproces.Nasdataccr().then(res => setSqldata(res))
            .catch(err => console.log(err)).finally(() => setLoading(false))

    }, [])

    useEffect(() => {
        if (Target.length > 0) {
            const payload = { "Clicks": Target }
            const interva = setInterval(() => {
                Axiosproces.Mikrotikreq(payload)
                    .then(res => setMikda(res))
                    .catch(err => console.log(err))
                    .finally(() => setLoading(false))

            }, 5000)
            return () => {

                clearInterval(interva)
                setMikda([])
            }
        }

    }, [Target])
    const clicks = (e) => {
        setLoading(true)
        setTarget(e)
        setactiveItem({ activeItem: e })
    }

    return (
        <>
            <Tabs onChange={clicks} type="card">
                {Sqldata.map((e) => (
                    <TabPane tab={e} key={e}></TabPane>
                ))}
            </Tabs>

            <List
                loading={Loading}
                grid={{
                    gutter: 16,
                    xs: 1,
                    sm: 2,
                    md: 4,
                    lg: 4,
                    xl: 6,
                    xxl: 4,

                }}
                rowKey={Math.random()}

                dataSource={Mikda}
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
                                    <div> Wireless Disable  {item.wireless[0]['Wireless_Disable'] !== 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
                                    <div> Ethernet Disable  {item.Ethernet[0]['Ethernet_Disable'] !== 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
                                    <div> Wireless Running  {item.wireless[0]['Wireless_Running'] === 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
                                    <div> Ethernet Running  {item.Ethernet[0]['Ethernet_Running'] === 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
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
                                        <td>Anlik Download / Anlik Upload </td>
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
                                        <td>Yazilim </td>
                                        <td></td>
                                        <td className="text-right"> {item.system[0]['Firmware']} </td>
                                    </tr>
                                    <tr>
                                        <th scope="row"></th>
                                        <td>Wlan Mode / Wlan Channel</td>
                                        <td></td>
                                        <td className="text-right"> {item.wireless[0]['Wireless_Mode']} / {item.wireless[0]['Wireless_Band']} </td>
                                    </tr>
                                    <tr>
                                        <th scope="row"></th>
                                        <td>Wlan Frequency / Scan List</td>
                                        <td></td>
                                        <td className="text-right">{item.wireless[0]['Wireless_Frequency']} / {item.wireless[0]['Wireless_wscanList']} </td>
                                    </tr>

                                    <tr>
                                        <th scope="row"></th>
                                        <td> Sinyal Kuvveti Rx</td>
                                        <td></td>

                                        <td className="text-right">{item.wireless[0]['Signal']["Signal1"]} / {item.wireless[0]['Signal']["Signal3"]} <WifiIndicator strength={DBMToSignalStrength(item.wireless[0]['Signal']["Signal1"])} /></td>
                                    </tr>
                                    <tr>
                                        <th scope="row"></th>
                                        <td>Sinyal Kuvveti Tx</td>
                                        <td></td>
                                        <td className="text-right">{item.wireless[0]['Signal']["Signal2"]} / {item.wireless[0]['Signal']["Signal4"]} <WifiIndicator strength={DBMToSignalStrength(item.wireless[0]['Signal']["Signal2"])} /></td>
                                    </tr>
                                </tbody>
                            </table>
                        </Card>
                    </List.Item>)} />


        </>
    )
}

export default Mikrotik
