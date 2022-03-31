#!/usr/bin/env python3
import os

import aws_cdk as cdk

from ecs_jenkins_slave.ecs_jenkins_slave_stack import EcsJenkinsSlaveStack

app = cdk.App()
EcsJenkinsSlaveStack(app, "EcsJenkinsSlaveStack",
    env=cdk.Environment(account='936820862755', region='us-east-1')
)

app.synth()
