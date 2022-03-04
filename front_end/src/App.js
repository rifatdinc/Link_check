/* eslint-disable jsx-a11y/anchor-is-valid */
import React from 'react'
import { ConfigProvider, Layout, Menu } from 'antd';
import Mimosa from './Component/Mimosa/Mimosa';
import Mikrotik from './Component/Mikrotik/Mikrotik5ghz'
import { Link, Route, Routes, useNavigate } from 'react-router-dom'
import Mik60Ghz from './Component/Mikrotik/Mik60Ghz'
import Ubnt60ghz from './Component/Ubuquiti/Ubnt60ghz';
import SignalScan from './Component/Mikrotik/SignalScan'
import Arizabul from './Component/Mikrotik/Fail_find';
import Ubnt5gHz from './Component/Ubuquiti/Ubnt5ghz';
import Speaksignal from './Component/SpeakSignal/Speak';
import Login from './Login/Login';
// import Axiosps from './Component/ManageRequest/Axiosps'
import jwt_decoder from 'jwt-decode';
const { SubMenu } = Menu;

const { Header, Content } = Layout;


const App = () => {
  let history = useNavigate();


  if (!localStorage.getItem('tokens')) {
    return <Login />
  }

  const jwt = localStorage.getItem('tokens')
  const Jwttoken = (jwt_decoder(jwt))
  console.log(Jwttoken)
  return (
    <>
      <ConfigProvider >

        <Layout style={{backgroundColor:"black"}}>
          <Header className="header"  style={{backgroundColor:"black"}}>
            <div className="logo" />

            <Menu  mode="horizontal" defaultSelectedKeys={['2']} >
              {Jwttoken.Role === 'Teknisyen' ? <><SubMenu key="SubMenu" title="Linkler">
                <Menu.Item key="setting:1"><Link to="/mimosa">Mimosa</Link></Menu.Item>
                <Menu.Item key="setting:2"><Link to="/Mikrotik">Mikrotik 5 gHz</Link></Menu.Item>
                <Menu.Item key="setting:3"><Link to="/Ubnt5gHz"> </Link>Ubnt 5 gHz</Menu.Item>
                <Menu.Item key="setting:5"><Link to="/Mik60ghz">60 Ghz Linkler</Link></Menu.Item>
                <Menu.Item key="setting:6"><Link to="/ubnt60ghz">Ubnt 60 Ghz</Link></Menu.Item>
              </SubMenu>
                <Menu.Item key="setting22"><Link to="/konustur"> </Link>Sinyal Söyle</Menu.Item>
                <Menu.Item key="setting55"><Link to="/signalscan"> </Link>Musteri Tarama</Menu.Item>
                <Menu.Item key="setting222"><Link to="/Arizabul"> </Link>Ariza Bul</Menu.Item>
              </> :
                <Menu.Item key="setting23"><Link to="/konustur"> </Link>Sinyal Söyle</Menu.Item>
              }


              <Menu.Item >
                <div onClick={() => {
                  history("/Login")
                  localStorage.removeItem("tokens")
                }} className="float-lg-right"> Cikis Yap</div>
              </Menu.Item>
            </Menu>



          </Header>
        </Layout>
        <Content  style={{ backgroundColor:"black", padding: '0 50px' }}>
          <Routes >
            <Route element={<SignalScan />} path="/signalscan" />
            <Route element={<Mimosa />} path="/mimosa" />
            <Route element={<Mikrotik />} path="/Mikrotik" />
            <Route element={<Mik60Ghz />} path="/Mik60Ghz" />
            <Route element={<Ubnt60ghz />} path="/ubnt60ghz" />
            <Route element={<Arizabul />} path="/Arizabul" />
            <Route element={<Ubnt5gHz />} path="/Ubnt5gHz" />
            <Route element={<Speaksignal />} path="/konustur" />
          </Routes>
        </Content>
      </ConfigProvider>

    </>

  )
}

export default App
