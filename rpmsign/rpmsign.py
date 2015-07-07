import xml.etree.ElementTree as XML

def rpmsign(parser, xml_parent, data):
    """yaml: rpmsign
    This plugin adds a post-build step to sign rpms using GPG.

    Requires the Jenkins `RPM Sign Plugin.
    <https://wiki.jenkins-ci.org/display/JENKINS/RPM+Sign+Plugin>`_
    :arg list rpms:
        :rpms:
            * **gpgKeyName** (`str`) - Name of the gpg key
            * **includes** (`str`) - Path to the rpm(s) sign
            * **cmdlineOpts** (`str`) - Optional command line options to rpmsign
            * **resign** (`bool`) -Resign the rpm 
                (default false)

    Example:
    .. literalinclude:: /../../sample/job.yaml
    """
    rpm_sign = XML.SubElement(xml_parent, 
        "jenkins.plugins.rpmsign.RpmSignPlugin"
    )

    entries = XML.SubElement(rpm_sign, 'entries')

    for entry in data['rpms']:
        rpm = XML.SubElement(entries, 'jenkins.plugins.rpmsign.Rpm')
        XML.SubElement(rpm, 'gpgKeyName').text = entry['gpgKeyName']        
        XML.SubElement(rpm, 'includes').text = entry['includes']
        XML.SubElement(rpm, 'cmdlineOpts').text = entry.get('cmdlineOpts', '')
        XML.SubElement(rpm, 'resign').text = str(entry.get('resign', False)).lower()

