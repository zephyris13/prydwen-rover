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

  translateMotion = (diry, force, angle) => {
    //      90
    //     /---\
    // 180 |   | = 0-360
    //     \___/
    //      270
    var output = [0, 0, 0, 0];
    const angleNorm = Math.round(Math.min(angle, 360));
    const forcePerc = Math.round(Math.min(force, 1) * 100);
    let turningRatio = 0;

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

      // quadrants
      if (0 < angleNorm && angleNorm < 90) {
        // Right Quadrant Top
        turningRatio = angleNorm / 90;
        output[3] = turningRatio;
        output[2] = 1;
      } else if (270 < angleNorm && angleNorm < 360 ) {
        // Right Quadrant Bottom
        turningRatio = (angleNorm - 270) / 90;
        output[3] = 1 - turningRatio;
        output[2] = 1;
      } else if (90 < angleNorm && angleNorm < 180) {
        // Left Quadrant Top
        turningRatio = (angleNorm - 90) / 90;
        output[2] = 1 - turningRatio;
        output[3] = 1;
      } else if (180 < angleNorm && angleNorm < 270) {
        // Left Quadrant Bottom
        turningRatio = (angleNorm - 180) / 90;
        output[2] = turningRatio;
        output[3] = 1;
      }
    }

    output[2] = Math.round(output[2] * 100);
    output[3] = Math.round(output[3] * 100);

    output[2] = Math.round((forcePerc / 100) * output[2]);
    output[3] = Math.round((forcePerc / 100) * output[3]);

    return output;
  }

  handleMove = (event, data) => {
    var output = [0, 0, 0, 0];

    if (event.type !== "end") {
      const diry = data.direction ? data.direction.y : "";
      const force = data.force;
      const angle = data.angle.degree;
      output = this.translateMotion(diry, force, angle);
    } else {
      output = [0, 0, 0, 0];
    }

    this.props.mqttClient.publish(Config["topicA"], `${output[0]} ${output[1]} ${output[2]} ${output[3]}`);
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
                  onEnd={(evt, data) => this.handleMove(evt, data)}
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