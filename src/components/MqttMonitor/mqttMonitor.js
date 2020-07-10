import Paper from "@material-ui/core/Paper";
import React, { Component } from "react";
import PropTypes from "prop-types";
import "../../App.css";

class MqttMonitor extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mqttClient: props.mqttClient,
      mqttConnected: false,
    };
  }

  componentDidUpdate(prevProps) {
    if (prevProps.mqttClient !== this.props.mqttClient
        && this.props.mqttClient !== undefined
        && !this.setState.mqttConnected) {
      this.setState({ mqttConnected: true });
      console.log("Mqtt connected!");
    }
    else if (this.props.mqttClient === undefined
      && this.setState.mqttConnected) {
      this.setState({ mqttConnected: false });
      console.log("Mqtt disconnected");
    }
  }

  render() {
    return (
      <Paper className="MqttMonitor">
        <p>Mqtt Status</p>
      </Paper>
    );
  }
}

MqttMonitor.propTypes = {
  mqttClient: PropTypes.object
};

export default MqttMonitor;