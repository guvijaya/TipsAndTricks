""" 
The code snippet provides quick overview on AML Pipelines.
The sample code could be executed from the AML Notebook.

The Pipeline (Published, Published End Point), Job, Experiment are consusing construct in AML
This online doc may help. https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer
"""
#----------------------------------------------------------------
# Running Experiment
#----------------------------------------------------------------
from azureml.core import Workspace, Experiment, Environment, ScriptRunConfig

ws = Workspace.from_config()
experiment = Experiment(workspace=ws, name='Experiment-001')

config = ScriptRunConfig(source_directory='./Users/guru/HW', script='Hello.py', compute_target='guru2') #guruAml

# TODO: Till code the path is already mounted. /mnt/batch/tasks/shared/LS_root/mounts/clusters/guru2/code/
# The path should resolve to /mnt/batch/tasks/shared/LS_root/mounts/clusters/guru2/code/Users/guru/HW/Users/guru/HW

run = experiment.submit(config)

# Log metrics
run.log('mymetric', 1)

# Check progress
run.wait_for_completion(show_output=True, wait_post_processing=True)
aml_url = run.get_portal_url()
print(aml_url)



#----------------------------------------------------------------
# Create pipeline and execute
#----------------------------------------------------------------
from azureml.core import Workspace, Experiment
from azureml.pipeline.core import Pipeline

# To know all other type of steps 
# https://docs.microsoft.com/en-us/python/api/azureml-pipeline-steps/azureml.pipeline.steps?view=azure-ml-py
from azureml.pipeline.steps import PythonScriptStep 

ws = Workspace.from_config()

#Define
pythonScriptStep = PythonScriptStep(script_name="Hello.py",
                            compute_target="guru2",
                            source_directory='./Users/guru/HW/', # It copies the whole folder to create the step.
                            name="Hello py execution step")

pipeline = Pipeline(workspace=ws, steps=[pythonScriptStep])

#Executing the pipeline
experiment = Experiment(workspace=ws, name='Experiment-002')
pipeline_run1 = experiment.submit(pipeline)



#----------------------------------------------------------------
# Publish a pipeline
#----------------------------------------------------------------
published_pipeline = pipeline.publish(name="PublishedPipeline")
print(f"Name: {published_pipeline.name} \t Id: {published_pipeline.id}")



#----------------------------------------------------------------
# Running a published pipeline
#----------------------------------------------------------------
from azureml.core import Workspace, Experiment
from azureml.pipeline.core import PublishedPipeline

ws = Workspace.from_config()

experiment = Experiment(workspace=ws, name='Experiment-001')

 # Everytime you publish a pipeline new Id created. So this part requires an update if you want to call a new version of the pipeline
published_pipeline = PublishedPipeline.get(workspace=ws, id=published_pipeline.id)
pipeline_run = experiment.submit(published_pipeline )



#----------------------------------------------------------------
# Creating a Pipeline End Point
#----------------------------------------------------------------
ws = Workspace.from_config()

experiment = Experiment(workspace=ws, name='Experiment-001')

from azureml.pipeline.core import PipelineEndpoint

published_pipeline = PublishedPipeline.get(workspace=ws, id=published_pipeline.id)

# The pipeline argument can be either a Pipeline or a PublishedPipeline
pipeline_endpoint = PipelineEndpoint.publish(workspace=ws,
                                            name="PipelineEndpoint-001",
                                            pipeline=published_pipeline,
                                            description="PipelineEndpoint-001")



#----------------------------------------------------------------
# Execute Pipeline Endpoint
#----------------------------------------------------------------
from azureml.pipeline.core import PipelineEndpoint

pipeline_endpoint = PipelineEndpoint.get(workspace=ws, name="PipelineEndpoint-001")
pipeline_run = experiment.submit(pipeline_endpoint)



#----------------------------------------------------------------
# Adding pipeline to existing Pipeline Endpoint
#----------------------------------------------------------------
# Publish new Pipeline
published_pipeline2 = pipeline.publish(name="PublishedPipeline2")
print(f"Name: {published_pipeline2.name} \t Id: {published_pipeline2.id}")

# Add the new Pipeline to existing Pipeline Endpoint
published_pipeline = PublishedPipeline.get(workspace=ws, id=published_pipeline2.id)
pipeline_endpoint = PipelineEndpoint.get(workspace=ws, name="PipelineEndpoint-001")
pipeline_endpoint.add(published_pipeline)

# Ensure the new version is set to default, it needs to be done explicitly
pipeline_endpoint.set_default(published_pipeline) 



#----------------------------------------------------------------
# Switching the default Pipeline in the Pipeline End Point
#----------------------------------------------------------------
pipeline_endpoint = PipelineEndpoint.get(workspace=ws, name="PipelineEndpoint-001")

# Switching using Version
#print(pipeline_endpoint.default_version)
#pipeline_endpoint.set_default_version("1")

#pipeline_id = published_pipeline.id
pipeline_id = published_pipeline2.id

# Switching using Id
published_pipeline = PublishedPipeline.get(workspace=ws, id=pipeline_id)
pipeline_endpoint.set_default(published_pipeline)
