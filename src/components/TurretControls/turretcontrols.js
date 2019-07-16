import Grid from "@material-ui/core/Grid";
import Paper from "@material-ui/core/Paper";
import Button from "@material-ui/core/Button";
import ExpandLess from "@material-ui/icons/ExpandLess";
import ExpandMore from "@material-ui/icons/ExpandMore";
import ChevronLeft from "@material-ui/icons/ChevronLeft";
import ChevronRight from "@material-ui/icons/ChevronRight";
import MyLocation from "@material-ui/icons/MyLocation";
import React, { Component } from "react";
import PropTypes from "prop-types";
import Config from "../../config.json";
import "../../App.css";

class TurretControls extends Component {
  constructor(props) {
    super(props);
    this.state = {
      mqttClient: props.mqttClient,
      spoolupChecked: false,
      mqttConnected: false,
      mouseDownIntervalHandler: undefined,
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

  handleChange = name => event => {
    this.setState({ [name]: event.target.checked });
    const message = !this.state.spoolupChecked;
    console.log(message);
    this.props.mqttClient.publish(Config["topicB"], JSON.stringify(message ? 1 : 0));
  };

  handleFire = () => {
    this.props.mqttClient.publish(Config["topicC"], JSON.stringify(1));
    setTimeout(() => { this.props.mqttClient.publish(Config["topicC"], JSON.stringify(0)); }, 1000);
  }

  handleMouseDown = (buttonId) => {
    const intervalHandler = setInterval(() => { this.mouseDownWorker(buttonId); }, 100);
    this.setState({ mouseDownIntervalHandler: intervalHandler });
    return false;
  }

  handleMouseUp = (buttonId) => {
    clearInterval(this.state.mouseDownIntervalHandler);
    this.setState({ mouseDownIntervalHandler: undefined });
  }

  mouseDownWorker = (buttonId) => {
    switch(buttonId) {
      case 0:
        this.props.mqttClient.publish(Config["topicA"], "90 -180");
        break;
      case 1:
        this.props.mqttClient.publish(Config["topicA"], "180 90");
        break;
      case 2:
        this.props.mqttClient.publish(Config["topicA"], "90 180");
        break;
      case 3:
        this.props.mqttClient.publish(Config["topicA"], "-180 90");
        break;
      default:
        return false;
    }
    return false;
  }

  render() {
    return (
      <Paper className="Controls">
        <p>Controls</p>

        <Grid item xs={12} style={{ paddingBottom: "40px" }}>     
          <Grid item xs={12}>
            <Button color="default" onMouseDown={() => { this.handleMouseDown(0); }} onMouseUp={() => { this.handleMouseUp(0); }}>
              <ExpandLess/>
            </Button>
          </Grid>

          <Grid item xs={12}>
            <Button color="default" onMouseDown={() => { this.handleMouseDown(3); }} onMouseUp={() => { this.handleMouseUp(3); }}>
              <ChevronLeft/>
            </Button>

            <Button color="default" onClick={() => { this.handleFire(); }}>
              <MyLocation/>
            </Button>

            <Button color="default" onMouseDown={() => { this.handleMouseDown(1); }} onMouseUp={() => { this.handleMouseUp(1); }}>
              <ChevronRight/>
            </Button>
          </Grid>

          <Grid item xs={12}>
            <Button color="default" onMouseDown={() => { this.handleMouseDown(2); }} onMouseUp={() => { this.handleMouseUp(2); }}>
              <ExpandMore/>
            </Button>
          </Grid>

        </Grid>
      </Paper>
    );
  }
}

TurretControls.propTypes = {
  mqttClient: PropTypes.object
};

export default TurretControls;