from astropy.table import Table
import numpy as np
"""Script creates pair of galaxies in the format of catsim galaxy catalog.
The central galaxy is picked at random form the OneDegSq.fits catsim catalog.
The size , location and ellipticity of the second galaxy can be manually
entered by the user.
The total field is assumed to be centered at the central galaxy.
"""


def get_galaxies():
    """Returns galaxy pairs fom the template catsim catalog"""
    cat = Table.read('data/gal_pair_temp_catalog.fits', format='fits')
    return cat


def get_a_b(e, hlr):
    """Returns semimajor/minor axis from ellipticity and HLR"""
    q = (1 - e) / (1. + e)
    b = hlr
    a = b / q
    return a, b


def get_hlr(a, b):
    """Returns HLR from semimajor and minor axis"""
    hlr = (a * b)**0.5
    return hlr


def update_mag(cat, Args):
    """Changes the magnitude in ugrizy band based on how the flux of second
    galaxy changes.
    """
    bands = ['u', 'g', 'r', 'i', 'z', 'y']
    for band in bands:
        cat[band + '_ab'][1] += -2.5 * np.log10(Args.flux_frac)


def get_second_galaxy(Args, cat):
    """Assigns center and bulge, dic sizes and flux of the second galaxy
    tp the input catalog
    """
    cat['ra'][1] = cat[0]['ra'] + Args.x0 * 0.2 / 3600.
    cat['dec'][1] = cat[0]['dec'] + Args.y0 * 0.2 / 3600.
    cat['fluxnorm_bulge'][1] = cat['fluxnorm_bulge'][1] * Args.flux_frac
    cat['fluxnorm_disk'][1] = cat['fluxnorm_disk'][1] * Args.flux_frac
    update_mag(cat, Args)
    # From ellipticity and HLR compute a, b
    hlr = get_hlr(cat['a_b'][0], cat['b_b'][0])
    cat['a_b'][1], cat['b_b'][1] = get_a_b(Args.b_e, hlr * Args.bhlr_frac)
    hlr = get_hlr(cat['a_d'][0], cat['b_d'][0])
    cat['a_d'][1], cat['b_d'][1] = get_a_b(Args.d_e, hlr * Args.dhlr_frac)
    cat['pa_disk'][1] = Args.p_angle
    cat['pa_bulge'][1] = Args.p_angle
    cat['galtileid'][1] = 1


def main(Args):
    # Get a catlog entry from One square degree catalog
    catalog = get_galaxies()
    # Add input properties of second galaxy to the catalog
    get_second_galaxy(Args, catalog)
    catalog.write('data/gal_pair_catalog.fits', format='fits', overwrite=True)
    catalog[0:1].write('data/gal1_catalog.fits', format='fits', overwrite=True)
    catalog[1:2].write('data/gal2_catalog.fits', format='fits', overwrite=True)


if __name__ == "__main__":
    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--flux_frac', default=1., type=float,
                        help="Flux of second galaxy as a fraction of \
                        central galaxy flux [Default:1]")
    parser.add_argument('--bhlr_frac', default=1., type=float,
                        help="HLR of second galaxy bulge as a fraction of \
                        central galaxy bulge HLR [Default:1]")
    parser.add_argument('--dhlr_frac', default=1., type=float,
                        help="HLR of second galaxy disk as a fraction of \
                        central galaxy disk HLR [Default:1]")
    parser.add_argument('--x0', default=6., type=float,
                        help="x coordinate of center of second galaxy in pixels. \
                        Center of central galaxy is (0,0).[Default:6]")
    parser.add_argument('--y0', default=6., type=float,
                        help="y coordinate of center of second galaxy in pixels. \
                        Center of central galaxy is (0,0). [Default:6]")
    parser.add_argument('--p_angle', default=0., type=float,
                        help="Position of center of second galaxy in degrees \
                        [Default:20]")
    parser.add_argument('--b_e', default=0., type=float,
                        help="Ellipticity (e) second galaxy bulge \
                        [Default:0.]")
    parser.add_argument('--d_e', default=0., type=float,
                        help="Ellipticity (e) second galaxy disk \
                        [Default:0.]")
    args = parser.parse_args()
    main(args)
