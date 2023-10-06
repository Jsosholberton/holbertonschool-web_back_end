export default function getListStudentIds(datas) {
  if (typeof datas === 'object') {
    return datas.map((data) => data.id);
  }
  return [];
}
