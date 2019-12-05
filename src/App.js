import Grid from "@material-ui/core/Grid";
import RobotView from "./components/RobotView/robotview";
import AttachmentView from "./components/AttachmentView/attachmentview";
import TurretControls from "./components/TurretControls/turretcontrols";
import DriveControls from "./components/DriveControls/drivecontrols";
import Mqtt from "mqtt";
import React, { Component } from "react";
import Config from "./config.json";
import "./App.css";

class App extends Component {

  state = {
    mqttUrl: "ws://" + Config["device_host"] + ":" + Config["mqtt_port"],
  };

  componentDidMount() {
    this.setupMqtt();
  }

  setupMqtt() {
    const client = Mqtt.connect(this.state.mqttUrl);

    client.on("connect", () => {
      this.setState({
        mqttClient: client
      });
    })

    client.on("close", () => {
      this.setState({
        mqttClient: undefined
      });
    })
  };

  render() {
    return (
      <div className="App App-background">
        <Grid container spacing={24}>

          <Grid item xs={1} />
          <Grid item xs={10}>
          </Grid>
          <Grid item xs={1} />

          <Grid item xs={1} />
          <Grid item xs={3}>
            <TurretControls mqttClient={this.state.mqttClient} />
          </Grid>
          <Grid item xs={4}>
            <AttachmentView />
          </Grid>
          <Grid item xs={3}>
            <DriveControls mqttClient={this.state.mqttClient} />
          </Grid>
          <Grid item xs={1} />

        </Grid>
      </div>
    );
  }
}

export default App;
