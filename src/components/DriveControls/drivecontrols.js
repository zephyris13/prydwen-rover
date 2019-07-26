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

  translateMotion = (dirx, diry, force, angle) => {
    // /---\
    // |   | = 0-359  
    // \___/
    const output = [0, 0, 0, 0];
    const angleNorm = Math.round(Math.min(angle, 360));
    const forcePerc = Math.round(Math.min(force, 1) * 100);

    if (forcePerc > 10) {

      if (diry.toLowerCase() === "up") {
        output[0] = 1;
        output[1] = 1;
      } else if (diry.toLowerCase() === "down") {
        output[0] = -1;
        output[1] = -1;
      } else {
        output[0] = 0;
        output[1] = 0;
      }

      
      
    }
    console.log(`${output} - ${angleNorm}`);
    return;
  }

  handleMove = (event, data) => {
    const dirx = data.direction ? data.direction.x : "";
    const diry = data.direction ? data.direction.y : "";
    const force = data.force;
    const angle = data.angle.degree;
    this.translateMotion(dirx, diry, force, angle);
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