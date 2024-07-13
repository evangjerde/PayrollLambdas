import aws_cdk as core
import aws_cdk.assertions as assertions

from payroll_lambdas.payroll_lambdas_stack import PayrollLambdasStack

# example tests. To run these tests, uncomment this file along with the example
# resource in payroll_lambdas/payroll_lambdas_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = PayrollLambdasStack(app, "payroll-lambdas")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
