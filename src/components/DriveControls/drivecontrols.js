import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import React, { Component } from "react";
import ReactNipple from 'react-nipple';
import PropTypes from "prop-types";
import Config from "../../config.json";
import "../../App.css";

class DriveControls extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mqttClient: props.mqttClient,
      DriveControlsChecked: false,
      mqttConnected: false
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

  handleMove = (event, data) => {
    const dirx = data.direction ? data.direction.x : "";
    const diry = data.direction ? data.direction.y : "";
    const force = Math.min(data.force, 1);
    const angle = data.angle.degree;
    console.log(`${dirx} - ${diry} - ${force} - ${angle}`);
  }

  render() {
    return (
        <Paper className="DriveControls" style={{backgroundColor: "gray"}}>
        <div>
          <p>Drive Controls</p>
          <Grid item xs={12} style={{ paddingBottom: "10px" }}>
            <Grid item xs={12} style={{position: "relative"}}>
              <ReactNipple
                  options={{ mode: 'static', position: { top: '50%', left: '50%'} }}
                  style={{
                      border: '1px dashed red',
                      borderRadius: '50%',
                      width: 150,
                      height: 150,
                      margin: '0 auto'
                  }}
                  onMove={(evt, data) => this.handleMove(evt, data)}
              />
            </Grid>
            <Grid item xs={12} />
          </Grid>
        </div>
        </Paper>
      );
    }
  }
  
  export default DriveControls;