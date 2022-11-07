terraform {
  required_providers {
    linode = {
        source = "linode/linode"
        version = "1.29.4"
    }
  }
}


provider "linode" {
    token = var.token
}


resource "linode_instance" "terraform-web" {
        image = "linode/ubuntu18.04"
        label = "Terraform-Example"
        group = "Terraform"
        region = "eu-central"
        type = "g6-standard-1"
        # authorized_keys = [ "YOUR_PUBLIC_SSH_KEY" ]
        root_pass = var.root_pass
        provisioner "local-exec" {
            command = "ANSIBLE_HOST_KEY_CHECKING=False ansible-playbook --extra-vars 'ansible_user=root ansible_password=${var.root_pass}' -i '${self.ip_address},' ansible.yaml"
        
        }
}

