from kuleuven.sitedelegation.browser.sharing import LocalSharingView

class EFSharingView(LocalSharingView):
    def roles(self):
        # Get the default roles from the base class
        roles = super().roles()
        
        # Check if the context is an EasyForm
        if self.context.portal_type == 'EasyForm':
            # Add the custom role if not already present
            if 'Data manager' not in [r['id'] for r in roles]:
                roles.append({
                    'id': "Data manager",
                    'title': "Access Easyform data",
                    'required': False,
                })
        else:
            # Remove the EasyFormsManager role for other content types
            roles = [r for r in roles if r['id'] != 'Data manager']
        
        return roles