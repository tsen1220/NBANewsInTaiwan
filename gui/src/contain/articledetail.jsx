import React from "react";
import axios from "axios";
import { Card } from "antd";

const { Meta } = Card;

class ArticleDetail extends React.Component {
  state = {
    article: {}
  };

  //axios.get
  componentDidMount() {
    const articleID = this.props.match.params.articleID;
    axios.get(`http://127.0.0.1:8000/api/article/${articleID}`).then(res => {
      this.setState({
        article: res.data
      });
    });
  }

  render() {
    return (
      <div>
        <Card
          hoverable
          style={{ width: 800 }}
          cover={<img alt="NBAnews" src={this.state.article.img} />}
        >
          <div className="title" style={{ fontSize: 30 }}>
            {this.state.article.title}
          </div>
          <br />
          <Meta
            description={this.state.article.content}
            style={{ fontSize: 18, width: 700 }}
          />
        </Card>
      </div>
    );
  }
}

export default ArticleDetail;
