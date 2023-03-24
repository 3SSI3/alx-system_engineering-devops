#!/usr/bin/pup
# Installing a specific ver of flask (2.1.0)
package {'flask':
	ensure   => '2.1.0',
	provider => 'pip'
}
