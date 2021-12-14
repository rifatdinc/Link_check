import React from 'react'
import { Layout, Menu } from 'antd';
import Sqlnas from './Components/ReturnData';
import Mikrotik from './Components/Mikrotik'
import { BrowserRouter, Link, Route } from 'react-router-dom'
import Mik60Ghz from './Components/Mik60ghz'
import Ubnt60ghz from './Component/Ubuquiti/Ubnt60ghz';
import signalscan from './Components/Mikrotikislemleri/Signalscan'
import Arizabul from './Components/Mikrotikislemleri/Arizabul';
import Ubnt5gHz from './Components/Ubnt5gHz';
import Zorlakonusutur from './Components/Sinyalkonusturma/Zorlakonusutur';
const { SubMenu } = Menu;

// import 'react-router-dm'
const { Header, Content } = Layout;

const App = () => {


  return (
    <div >
      <BrowserRouter>
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
          <Route component={signalscan} path="/signalscan" />
          <Route component={Sqlnas} path="/mimosa" />
          <Route component={Mikrotik} path="/Mikrotik" />
          <Route component={Mik60Ghz} path="/Mik60Ghz" />
          <Route component={Ubnt60ghz} path="/ubnt60ghz" />
          <Route component={Arizabul} path="/Arizabul" />
          <Route component={Ubnt5gHz} path="/Ubnt5gHz" />
          <Route component={Zorlakonusutur} path="/konustur" />
        </Content>
      </BrowserRouter>
    </div>
  )
}

export default App
