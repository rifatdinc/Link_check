import React, { useState, useEffect } from 'react';
import { Form, Select } from 'antd';
import Axiosps from '../Axioss/Axiosprocess'

/* eslint-disable no-template-curly-in-string */
const { Option } = Select;

/* eslint-enable no-template-curly-in-string */

const Arizabul = () => {
    const [Orm, setOrm] = useState([])
    useEffect(() => {
        Axiosps.Nasdataccr()
        .then(res => setOrm(res))
        .catch(err => console.log(err))
    }, [])


    const startRun = () => {
        return document.getElementById('Nasselect').parentElement.parentElement.lastChild.title
    }
    



    return (
        <div className="container p-3">
            <h1 className="text-center">Musteri Ariza Bul</h1>
            <Form.Item
                name="Nasselect"
                label="Router Seciniz">
                <Select>
                    {Orm.map((e) => {
                        return <Option id="Namikkemal" key={e}>{e}</Option>
                    })}

                </Select>
            </Form.Item>
            {Orm.length > 0 ? <button onClick={startRun}>Dogru</button> : null}
        </div>
    );
};
export default Arizabul