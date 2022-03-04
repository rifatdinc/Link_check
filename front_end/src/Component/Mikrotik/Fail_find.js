import React, { useState, useEffect } from 'react';
import { Form, Select, Button } from 'antd';
import Axiosps from '../ManageRequest/Axiosps'


const Fail_find = () => {
    const [Orm, setOrm] = useState([])
    const [Result,setResult] =useState([])
    useEffect(() => {
        Axiosps.Nasdatavalue()
            .then(res => {
                setOrm(res)
            })
            .catch(err => console.log(err))
    }, [])


    const RequestEnd = (_value, key) => {
        setResult([...key])

    }
    const SubmitRequest = ()=>{
        Axiosps.Find_Fail(Result).then().catch().finally()
    }



    return (
        <div className="container p-3">
            <h1 className="text-center">Musteri Ariza Bul</h1>
            <Form >
                <Form.Item
                    name="Nasselect"
                    label="Router Seciniz">
                    <Select allowClear onChange={RequestEnd} mode="tags" options={Orm} />
                </Form.Item>
            </Form>
            <Button block onClick={SubmitRequest} type='primary' htmlType='submit'>Başlat</Button>

        </div>
    );
};
export default Fail_find