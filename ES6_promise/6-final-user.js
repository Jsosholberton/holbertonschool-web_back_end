import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
  firstName = '',
  lastName = '',
  fileName = '',
) {
  const prom = await Promise.allSettled([
    uploadPhoto(fileName),
    signUpUser(firstName, lastName),
  ]);
  return prom;
}
