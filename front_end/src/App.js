import React from 'react'
import { Layout, Menu } from 'antd';
import Mimosa from './Component/Mimosa/Mimosa';
import Mikrotik from './Component/Mikrotik/Mikrotik5ghz'
import { BrowserRouter as Router, Link, Route, Routes, } from 'react-router-dom'
import Mik60Ghz from './Component/Mikrotik/Mik60Ghz'
import Ubnt60ghz from './Component/Ubuquiti/Ubnt60ghz';
import SignalScan from './Component/Mikrotik/SignalScan'
import Arizabul from './Component/Mikrotik/Fail_find';
import Ubnt5gHz from './Component/Ubuquiti/Ubnt5ghz';
import Speaksignal from './Component/SpeakSignal/Speak';
const { SubMenu } = Menu;

// import 'react-router-dm'
const { Header, Content } = Layout;
const App = () => {

  return (
    <>
      <div >
        <Router>
          <Layout>
            <Header className="header">
              <div className="logo" />
              <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                <SubMenu key="SubMenu" title="Linkler">
                  <Menu.Item key="setting:1"><Link to="/mimosa" >Mimosa</Link></Menu.Item>
                  <Menu.Item key="setting:2"><Link to="/Mikrotik" >Mikrotik 5 gHz</Link></Menu.Item>
                  <Menu.Item key="setting:3"><Link to="/Ubnt5gHz"> </Link>Ubnt 5 gHz</Menu.Item>
                  <Menu.Item key="setting:5"><Link to="/Mik60ghz">60 Ghz Linkler</Link></Menu.Item>
                  <Menu.Item key="setting:6"><Link to="/ubnt60ghz">Ubnt 60 Ghz</Link></Menu.Item>
                </SubMenu>
                <SubMenu key="Submenu1" title="Mikrotik Islemler">
                  <Menu.Item key="setting1"><Link to="/signalscan"> </Link>Musteri Tarama</Menu.Item>
                  <Menu.Item key="setting2"><Link to="/Arizabul"> </Link>Ariza Bul</Menu.Item>
                  <Menu.Item key="setting22"><Link to="/konustur"> </Link>Sinyal Söyle</Menu.Item>
                </SubMenu>
              </Menu>
            </Header>
          </Layout>
          <Content style={{ padding: '0 50px' }}>
            <Routes >
              <Route path="/signalscan" element={<SignalScan/>}  />
              <Route element={<Mimosa/>} path="/mimosa" />
              <Route element={<Mikrotik/>} path="/Mikrotik" />
              <Route element={<Mik60Ghz/>} path="/Mik60Ghz" />
              <Route element={<Ubnt60ghz/>} path="/ubnt60ghz" />
              <Route element={<Arizabul/>} path="/Arizabul" />
              <Route element={<Ubnt5gHz/>} path="/Ubnt5gHz" />
              <Route element={<Speaksignal/>} path="/konustur" />
            </Routes>
          </Content>
        </Router>

      </div>
    </>

  )
}

export default App
