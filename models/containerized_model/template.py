"""
Copyright (c) 2020. Cognitive Scale Inc. All rights reserved.
Licensed under CognitiveScale Example Code License https://github.com/CognitiveScale/cortex-certifai-examples/blob/master/LICENSE.md
"""
import argparse
import os
import stat
import shutil

from jinja2 import FileSystemLoader, Environment

CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))


def main():
    def create_directories(directory_list: list):
        for directory in directory_list:
            try:
                os.makedirs(os.path.join(BASE_DIR, directory))
            except FileExistsError:
                pass

    def generate_base_file_metadata():
        file_metadata = {
            'container_util.sh': {
                'exec_permission': True,
                'kwargs': {
                    'TARGET_DOCKER_IMAGE': args.target_docker_image
                }
            },
            'deployment.yml': {
                'exec_permission': False,
                'kwargs': {
                    'RESOURCE_NAME': args.k8s_resource_name,
                    'NAMESPACE': args.k8s_namespace
                }
            }
        }
        return file_metadata


    def apply_template(env, filename, exec_permission=False, **kwargs):
        _template = env.get_template(filename)
        rendered_template = _template.render(kwargs)
        file_path = os.path.join(BASE_DIR, filename)

        with open(file_path, 'w') as f:
            f.write(rendered_template)

        if exec_permission:
            _st = os.stat(os.path.join(BASE_DIR, filename))
            os.chmod(os.path.join(BASE_DIR, filename), _st.st_mode | stat.S_IEXEC)

    def apply_templates(template_path, file_metadata):
        file_loader = FileSystemLoader(os.path.join(CURRENT_PATH, template_path))
        env = Environment(loader=file_loader)
        for filename, value in file_metadata.items():
            apply_template(env, filename, value.get('exec_permission'), **value.get('kwargs'))

    def generate_base(model_type):
        directory_names = {'src', 'model'}
        create_directories(list(directory_names))

        # Common templates
        apply_templates('templates', generate_base_file_metadata())

        # Model-specific templates
        file_metadata = {
            'environment.yml': {
                'exec_permission': False,
                'kwargs': {}
            },
            'Dockerfile': {
                'exec_permission': False,
                'kwargs': {
                    'BASE_DOCKER_IMAGE': args.base_docker_image
                }
            },
            'src/prediction_service.py': {
                'exec_permission': False,
                'kwargs': {}
            },
            'src/utils.py': {
                'exec_permission': False,
                'kwargs': {}
            },
            'requirements.txt': {
                'exec_permission': False,
                'kwargs': {}
            },
            'model/metadata.yml': {
                'exec_permission': False,
                'kwargs': {}
            },
        }
        apply_templates(f'templates/{model_type}', file_metadata)


    def generate_python(model_type):
        generate_base(model_type)

    def generate_h2o_mojo(model_type):
        generate_base(model_type)
        extra_directory_names = {'ext_packages', 'license'}
        create_directories(list(extra_directory_names))

    # Argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', help='Directory name to be created for the containerized model.')
    parser.add_argument('--base-docker-image', help='Base docker image for the containerized model.')
    parser.add_argument('--target-docker-image', help='Target docker image to be built.')
    parser.add_argument('--k8s-resource-name', help='Name to be used as name in k8s resources (service, deployment, etc.).')
    parser.add_argument('--k8s-namespace', help='Name to be used as namespace in k8s resources (service, deployment, etc.).')
    parser.add_argument('--model-type', help='Type of model you want to generate the code for. e.g h2o_mojo, python')
    args = parser.parse_args()

    # Base directory
    BASE_DIR = args.dir
    model_type = args.model_type
    valid_types = ['python', 'python_sklearn', 'h2o_mojo']
    if model_type not in valid_types:
        print(f"'--model-type' must be one of {valid_types}")
        exit(1)

    if args.model_type == 'h2o_mojo':
        generate_h2o_mojo(model_type)
    else:
        model_type = 'python_sklearn' if model_type == 'python' else model_type
        generate_python(model_type)

    # Copy readme into the generated directory
    readme_files = ['README.md', 'DEPLOYMENT.md']
    for readme in readme_files:
        shutil.copyfile(os.path.join(CURRENT_PATH, readme), os.path.join(BASE_DIR, readme))


if __name__ == '__main__':
    main()
