import React, { useEffect, useState } from 'react'
import { List, Card } from 'antd';
import WifiIndicator, { DBMToSignalStrength } from 'react-wifi-indicator';
import { Grid, Menu, Segment } from 'semantic-ui-react'
import Axiosproces from './Axioss/Axiosprocess'
const ReturnData = () => {
    const [Sqldata, setSqldata] = useState([])
    const [gelendata, setgelendata] = useState([])
    const [activeItem, setactiveItem] = useState({ activeItem: "Balturk 1" })
    const [Strinq, setStrinq] = useState("")
    const [Loadinqs, setLoadinqs] = useState(false)

    useEffect(() => {
        Axiosproces.Nasdataccr().then(res => setSqldata(res))
            .catch(err => console.log(err))

    }, [])


    const clicks = (e) => {
        setStrinq(e.target.innerText)
        let s1 = e.target.innerText.replace(" ", "")
        setactiveItem({ activeItem: s1 })
    }




    useEffect(() => {
        if (Strinq.length > 0) {
            const paylod = { "Clickdata": Strinq }
            setLoadinqs(true)

            const interva = setInterval(() => {
                // Axios ile gelen data burada set ediyorum. Mimosa Fonksiyonuyla.
                Axiosproces.Mimosa(paylod).then(res => {
                    if (res !== undefined) {
                        let le2ws = []
                        console.log(res);
                        res.forEach(element => {
                            if (element !== null) {
                                le2ws.push(element)
                            } 
                        });
                        setgelendata(le2ws)
                    }

                })
                setLoadinqs(false)
            }, 5000);

            return () => {
                clearInterval(interva)

                // Memory leak onlemek icin state'i bos diziye dondurmem gerekiyor.
                setgelendata([])
            }
        }

    }, [Strinq]);




    return (
        <div>

            <Grid>
                <Grid.Column width={2}>
                    <Menu fluid vertical tabular>
                        {Sqldata.map((e) => {
                            return <Menu.Item
                                name={e}
                                key={e}
                                active={activeItem['activeItem'] === e}
                                onClick={clicks}
                            />


                        })}

                    </Menu>
                </Grid.Column>

                <Grid.Column stretched width={14}>
                    <Segment>
                        <List
                            split={true}
                            loading={Loadinqs}

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
                            dataSource={gelendata}
                            renderItem={((item) => {

                                try {
                                    return <List.Item id="Cardbolumu" bordered="true" style={{ width: "450px" }} >
                                        <Card size="small">
                                            Cihaz Ip Adres :<a className="text-right" value={`http://${item.Data.MimosaIp}`} href={`http://${item.Data.MimosaIp}`}> {item.Data.MimosaIp}</a>
                                            <h6>
                                                Cihaz Isimi : {item.Data.NamesMimosa}
                                            </h6>
                                            <hr />
                                            <table className="table table-sm">
                                                <thead>
                                                    <tr>
                                                        <th scope="col"></th>
                                                        <th scope="col">Mhz</th>
                                                        <th scope="col"></th>
                                                        <th scope="col" className="text-right">{item.Data.MimosaMhz}</th>
                                                    </tr>
                                                </thead>
                                                <tbody>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td> Frekans </td>
                                                        <td></td>
                                                        <td className="text-right"> {item.Data.MimosaFrequency}</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Max Kapasite Download</td>
                                                        <td></td>
                                                        <td className="text-right"> {item.Data.MimosaTotalRxPhy} Mbps</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Max Kapasite Upload  </td>
                                                        <td></td>
                                                        <td className="text-right"> {item.Data.MimosaTotalTxPhy} Mbps</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Anlik Gecen Upload</td>
                                                        <td></td>
                                                        <td id="Txvalue21" className="text-right">{item.Data.MimosaTxValue} Mbps</td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Anlik Gecen Donwload </td>
                                                        <td></td>
                                                        <td id="Txvalue21" className="text-right"> {item.Data.MimosaRxValue} Mbps</td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td> Sinyal Kuvveti Rx</td>
                                                        <td></td>

                                                        <td className="text-right">{item.Data.RxDbm} <WifiIndicator strength={DBMToSignalStrength(item.Data.RxDbm)} /></td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Sinyal Kuvveti Tx</td>
                                                        <td></td>
                                                        <td className="text-right">{item.Data.RxDbm1}<WifiIndicator strength={DBMToSignalStrength(item.Data.RxDbm1)} /></td>
                                                    </tr>
                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Ethernet Hizi </td>
                                                        <td></td>
                                                        <td id="ethspeed" className="text-right"> {item.Data.Ethspeed === 100 ? <h5 style={{ color: "red" }}> {item.Data.Ethspeed} Mbps</h5> : <h6>{item.Data.Ethspeed} Mbps </h6>}  </td>
                                                    </tr>

                                                    <tr>
                                                        <th scope="row"></th>
                                                        <td>Cpu Sicaklik</td>
                                                        <td></td>
                                                        <td className="text-right"> <i className="fas fa-thermometer-quarter">{item.Data.MimosaCpuTemp} </i></td>
                                                    </tr>
                                                </tbody>
                                            </table>
                                        </Card>
                                    </List.Item>

                                } catch (error) {
                                    console.log(error);
                                }

                            })




                            }
                        />
                    </Segment>

                </Grid.Column>
            </Grid>
        </div>

    )
}

export default ReturnData

    // const Getdatasql = (payload) =>{
    //     axios.post('http://192.10.10.180:5000/getdatasql', payload)
    //             .then((res) => {
    //                 const lost = []
    //                 res.data.forEach(e => {
    //                     if (e !== null) {
    //                         console.log(e);
    //                         lost.push(e)
    //                     }
    //                 });
    //                 setgelendata(lost)
    //             }).catch((error) => console.log(error))
    // }


      // <div key={e} className="btn-group" role="group" aria-label="Basic example">
                            //     <button onClick={clicks} type="button" className="btn btn-warning border " >{e} </button>

                            // </div>