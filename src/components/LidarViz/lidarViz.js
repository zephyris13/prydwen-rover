import Paper from "@material-ui/core/Paper";
import React, { Component } from "react";
import Config from "../../config.json";
import "../../App.css";

class LidarViz extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mqttClient: props.mqttClient,
      mqttConnected: false
    };
  }

  componentDidUpdate(prevProps) {
    if (prevProps.mqttClient !== this.props.mqttClient
        && this.props.mqttClient !== undefined
        && !this.setState.mqttConnected) {
      this.setState({ mqttConnected: true });
    }
    else if (this.props.mqttClient === undefined
      && this.setState.mqttConnected) {
      this.setState({ mqttConnected: false });
    }
  }

  render() {
    return (
      <Paper className="Video">
        <p>Robot View</p>
        <img style={{ paddingBottom: "20px", width: "90%" }} src={this.state.cameraUrl} alt={this.state.cameraUrl} />
      </Paper>
    );
  }
}

LidarViz.propTypes = {
  mqttClient: PropTypes.object
};

export default LidarViz;