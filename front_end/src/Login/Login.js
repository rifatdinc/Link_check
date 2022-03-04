/* eslint-disable jsx-a11y/anchor-is-valid */
import React, { useState } from 'react';
import { Form, Input, Button ,Checkbox,Alert} from 'antd';
import Axiosps from '../Component/ManageRequest/Axiosps';
import { UserOutlined, LockOutlined, ExclamationCircleOutlined } from '@ant-design/icons';
import '../../node_modules/antd/dist/antd.css';
import './index.css'
import { useNavigate } from 'react-router-dom';
const Login = () => {
    const [loginLoading, setloginLoading] = useState(false)
    const [loginMessege,setloginMessege ] = useState('')
    let navigate = useNavigate();
    const onFinish = (values) => {
        console.log(values)
        Axiosps.Login(values).then(res => {
            if (res.access_token) {
                localStorage.setItem('tokens', res.access_token)
                navigate('/')
                // window.location.replace("/")
            } else {
                setloginLoading(true)
                setloginMessege(res.error)
                return false;
            }
            return;
        }).catch(err => {
            if (err.response.status > 400) {
                setloginLoading(false)
                // window.location.replace("/Login")
                return false;
            }
        })
    };
    
    const onFinishFailed = (errorInfo) => {
        console.log('Failed:', errorInfo);
    };


    return (
        <>
          <div className='bg-img'>
    
            <h1 >
              Borealis
            </h1>
    
            <Form
              name="normal_login"
              className="login-form"
              initialValues={{
                remember: true,
              }}
              onFinish={onFinish}
            >
              <Form.Item
                name="username"
                rules={[
                  {
                    required: true,
                    message: 'Kullanıcı adınızı giriniz!',
                  },
                ]}
              >
                <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username" />
              </Form.Item>
              <Form.Item
                name="password"
                rules={[
                  {
                    required: true,
                    message: 'Şifrenizi Giriniz!',
                  },
                ]}
              >
                <Input
                  prefix={<LockOutlined className="site-form-item-icon" />}
                  type="password"
                  placeholder="Password" />
              </Form.Item>
              <Form.Item>
                <Form.Item name="remember" valuePropName="checked" noStyle>
                  <Checkbox>Beni Hatırla</Checkbox>
                </Form.Item>
    
                <a  className="login-form-forgot" >
                  Şifremi Unuttum!
                </a>
              </Form.Item>
              <Form.Item>
                {loginMessege.length>0 && <Alert message={loginMessege} type="error" />}
                <Button loading={loginLoading} type="primary" htmlType="submit" className="login-form-button">
                  Giriş Yap
                </Button>
              </Form.Item>
            </Form>
          </div>
    
        </>
      );
};

export default Login;