import json
import pytest

from aws_cdk import core
from cdkworkshop.cdkworkshop_stack import CdkworkshopStack


def get_template():
    app = core.App()
    CdkworkshopStack(app, "cdkworkshop")
    return json.dumps(app.synth().get_stack("cdkworkshop").template)


def test_lambda_function_created():
    assert('AWS::Lambda::Function' in get_template())


def test_dynamodb_created():
    assert('AWS::DynamoDB::Table' in get_template())

def test_runtime_environment_version():
    assert('Runtime": "python3.8"')
