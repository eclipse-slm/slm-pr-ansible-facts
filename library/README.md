## Resources

- https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_general.html
- https://docs.ansible.com/ansible/latest/dev_guide/developing_modules_best_practices.html#developing-modules-best-practices
- https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html#argument-spec
- https://docs.ansible.com/ansible/latest/dev_guide/debugging.html#debugging-modules

## Prepare

Create facts file

````shell
ansible-playbook create_facts_file.yml
````

## Run module via python use facts.json

````shell
python aas.py facts.json
````

## Run module via ansible

In directory containing "library" folder:

````shell
ansible-playbook run_module.yml
````

... with run_module.yml:

````yaml
- name: Test Module
  hosts: localhost
  gather_facts: true
  tasks:
    - name: Run module
      my_test:
        name: hello
        new: true
      register: result

    - debug:
        var: result
````