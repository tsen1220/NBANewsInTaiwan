import React from "react";
import { List } from "antd";

const Article = props => {
  return (
    <List
      itemLayout="vertical"
      size="large"
      pagination={{
        onChange: page => {
          console.log(page);
        },
        pageSize: 7
      }}
      dataSource={props.data}
      footer={<div>NBA news</div>}
      renderItem={item => (
        <List.Item
          key={item.title}
          extra={<img width={272} alt="logo" src={item.img} />}
        >
          <List.Item.Meta
            title={<a href={"/" + item.id}>{item.title}</a>}
            description={item.description}
          />
          {item.time.slice(0, 4) +
            "-" +
            item.time.slice(4, 6) +
            "-" +
            item.time.slice(6, 8) +
            " " +
            item.time.slice(8, 10) +
            ":" +
            item.time.slice(10, 12)}
          <br />
          <br />
          {item.content.slice(0, 200) + "......."}
        </List.Item>
      )}
    />
  );
};
export default Article;
