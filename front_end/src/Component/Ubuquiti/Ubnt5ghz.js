import React, { useEffect, useState } from 'react';
import { List, Card, Row, Tabs, Col } from 'antd';
import WifiIndicator, { DBMToSignalStrength } from 'react-wifi-indicator';
import formatBytes from '../Formatbytes';
import secondsToDhms from './secondToDhms.js';
import Axiosps from '../ManageRequest/Axiosps';

const { TabPane } = Tabs;
const Ubnt5gHz = () => {
    const [ubnt5ghzdata, setubnt5ghzdata] = useState([]);
    const [Sqldata, setSqldata] = useState([]);
    const [Loading, setLoading] = useState(false);
    const [, setactiveItem] = useState({ activeItem: "Balturk2" });
    const [Target, setTarget] = useState('');


    useEffect(() => {
        // Sql Datalarini yonetmek icin axiosproces isimli
        // Modulumden Nasdatasini import edip burada kullaniyorum.
        Axiosps.Nasdataccr().then((res) => { setSqldata(res); });
    }, []);


    useEffect(() => {
        const payload = { "Clicks": Target };
        setLoading(true);
        if (Target.length > 0) {
            const interva = setInterval(() => {
                Axiosps.Ubnt5gHz(payload).then((res) => {
                    setubnt5ghzdata(res);
                }).catch(err => console.log(err)).finally(() => setLoading(false))
                .finally(() => setLoading(false));
            }, 5000);
            return () => {
                clearInterval(interva);
                setubnt5ghzdata([]);
            };
        }
        setLoading(false)



    }, [Target]);

    const clicks = (e) => {
        setTarget(e);
        setactiveItem({ activeItem: e });
    };


    return (
        <>
            <Tabs onChange={clicks} type="card">
                {Sqldata.map((e) => (
                    <TabPane tab={e} key={e}></TabPane>
                ))}
            </Tabs>

            < List
                loading={Loading}
                grid={{gutter:16,column:3}}
                dataSource={ubnt5ghzdata}
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
                                        <div> Ethernet Disable  {item.Data.Data1.interfaces[0].status['plugged'] === 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
                                        <div> Wireless Disable  {item.Data.Data1.interfaces[0].status['enabled'] === 'false' ? <i className="fas fa-times"></i> : <i className="fas fa-check"></i>}</div>
                                    </Col>
                                </Row>

                                <div style={{ fontSize: "12px" }} >Uptime {secondsToDhms(item.Data.Data1["host"]["uptime"])}</div>
                                <hr />
                                <table className="table table-sm">
                                    <thead>
                                        <tr>
                                            <th scope="col"></th>
                                            <th scope="col">Kapasite</th>
                                            <th scope="col"></th>
                                            <th scope="col" className="text-right"> {formatBytes(item.Data.Data1.wireless.sta[0].airmax.downlink_capacity + "000")} </th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Cihaz Modeli </td>
                                            <td></td>
                                            <td className="text-right">{item.Data.Data1["host"]["devmodel"]}</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Ethernet Hizi </td>
                                            <td></td>
                                            <td className="text-right">{item.Data.Data1.interfaces[0].status["speed"]}</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Frequency </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.wireless["frequency"]} gHz </td>
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
                                            <td className="text-right"> {item.Data.Data1.wireless['antenna_gain']} dBi</td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Tx Power </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.wireless['txpower']} dBi </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td> Mac Adress </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.interfaces[1]['hwaddr']} </td>
                                        </tr>

                                        <tr>
                                            <th scope="row"></th>
                                            <td>Uzaklik </td>
                                            <td></td>
                                            <td className="text-right">{item.Data.Data1.wireless.sta[0]["distance"]}  metre </td>
                                        </tr>
                                        <tr>
                                            <th scope="row"></th>
                                            <td>Wlan Mod </td>
                                            <td></td>
                                            <td className="text-right"> {item.Data.Data1.wireless['mode']}</td>
                                        </tr>

                                        <tr>
                                            <th scope="row"></th>
                                            <td> Sinyal Kuvveti Rx</td>
                                            <td></td>

                                            <td className="text-right">{item.Data.Data1.wireless.sta[0]["signal"]}  <WifiIndicator strength={DBMToSignalStrength(item.Data.Data1.wireless.sta[0]["signal"])} /></td>
                                        </tr>

                                    </tbody>
                                </table>
                            </Card>
                        </List.Item>
                    } catch (error) {
                        console.log(error, '----Error- Ubnt5ghz FAULT')
                    }



                })}
            />
        </>
    )
}

export default Ubnt5gHz



