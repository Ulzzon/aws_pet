from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as ddb,
    core,
)

class HitCounter(core.Construct):

    @property
    def handler(self):
        return self._handler

    def __init__(self, scope: core.Construct, id: str, downstream: _lambda.IFunction, **kwargs):
        super().__init__(scope, id, **kwargs)

        table = ddb.Table( self,
            'Hits',
            partition_key={'name': 'path', 'type': ddb.AttributeType.STRING},
        )

        self._handler = _lambda.Function(self,
            'HitCounterHandler',
            runtime= _lambda.Runtime.PYTHON_3_8,
            handler='hitcount.handler',
            code=_lambda.Code.asset('lambda'),
            environment={
                'DOWNSTREAM_FUNCTION_NAME': downstream.function_name,
                'HITS_TABLE_NAME': table.table_name,
            }
        )

        table.grant_read_write_data(self.handler)
        downstream.grant_invoke(self.handler)